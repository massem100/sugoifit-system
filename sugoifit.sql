/* SugoiFit Database */

DROP DATABASE IF EXISTS sugoifit;

CREATE DATABASE sugoifit;

USE sugoifit;

CREATE table user(
    userID VARCHAR(5) NOT NULL UNIQUE,
    fname VARCHAR(25),
    lname VARCHAR(25),
    user_address VARCHAR(50),
    phone VARCHAR(10),

    PRIMARY KEY(userID)
);
-- EDIT THESE TABLES




CREATE table Credentials(
    userID VARCHAR(5) NOT NULL UNIQUE, 
    role VARCHAR(10), 
    email VARCHAR(50) NOT NULL, 
    user_password VARCHAR(255), 
    pass_salt VARCHAR(50),
    
    PRIMARY KEY(email),
    FOREIGN KEY(userID) REFERENCES user(userID) 
    ON DELETE CASCADE 
    ON UPDATE CASCADE
    );



CREATE table Business(
    busID INT(10) NOT NULL unique, 
    busName VARCHAR(100),
    busemail VARCHAR(255), 
    busaddress VARCHAR(100), 
    telephone VARCHAR(100),
    
    PRIMARY KEY(busID)
);


CREATE table `FinancialStmt`(
    stmtID VARCHAR(10) NOT NULL unique, 
    fs_name VARCHAR(50), 
    PRIMARY KEY(stmtID)
   
);



CREATE table FinancialStmtLine(
    lineID INT(10) NOT NULL unique AUTO_INCREMENT, 
    line_name VARCHAR(200), 
    lineDesc VARCHAR(50), 
    tag varchar(50),
    sequence int, 
    fact int, 

    PRIMARY KEY (lineID)
    
);


CREATE table FinancialStmtDesc(
    fStmtDescID INT(15) NOT NULL unique,
    companyID INT(10) NOT NULL unique, 
    fsLineID INT(10) NOT NULL unique, 
    fiscalPeriod DATE,
    fillingDATE DATE ,
    fiscalYear INT(5),
    startDATE DATE, 
    endDATE DATE, 
    unit DECIMAL(10,2), 
    PRIMARY KEY(fStmtDescID, companyID, fsLineID),
    FOREIGN KEY  (fsLineID) REFERENCES FinancialStmtLine(lineID) on upDATE cascade on delete cascade,
    FOREIGN KEY  (companyID) REFERENCES Business(busID) on upDATE cascade on delete cascade
);





CREATE table FinancialStmtLineSeq(
    lineSeqID INT(5) NOT NULL AUTO_INCREMENT,
    fsStmtID VARCHAR(50) NOT NULL,     
    fsStmtLineID INT(10) NOT NULL, 
    sequence INT(10),

    PRIMARY KEY (lineSeqID, fsStmtID, fsStmtLineID),
    FOREIGN KEY (fsStmtID) REFERENCES FinancialStmt(stmtID) on upDATE cascade on delete cascade,
    FOREIGN KEY (fsStmtLineID) REFERENCES FinancialStmtLine(lineID) on upDATE cascade on delete cascade

);

CREATE table FinancialStmtLineAlias(
    lineID INT(10) NOT NULL unique, 
    fsStmtID VARCHAR(50) NOT NULL,
    aliasID INT(25) NOT NULL unique, 
    lineAlias VARCHAR(50),     
    PRIMARY KEY (lineID, aliasID),
    foreign key (lineID) REFERENCES FinancialStmtLine(lineID) on update cascade on delete cascade,
    foreign key (fsStmtID) REFERENCES FinancialStmt(stmtID) on update cascade on delete cascade

);



CREATE table AccountType(
    typeID VARCHAR(10) NOT NULL, 
    accountCategory VARCHAR(100),

    PRIMARY KEY(typeID)
);


CREATE table Account( 
    accountID VARCHAR(10) NOT NULL, 
    accountName VARCHAR(100), 
    typeID VARCHAR(10),

    PRIMARY KEY(accountID),
    FOREIGN KEY(typeID) REFERENCES AccountType(typeID)
    ON DELETE CASCADE
    ON UPDATE CASCADE

);

/*

CREATE table Voucher(
    vouchID VARCHAR(5) NOT NULL unique, 
    accountID VARCHAR(10), 
    vType ENUM('creditVoucher', 'debitVoucher'),  
    vDATE DATE, 
    authBy VARCHAR(10), 
    prepBy VARCHAR(10),

    PRIMARY KEY(vouchID),
    foreign key (accountID) REFERENCES Account(accountID) on update cascade on delete cascade,
    foreign key (authBy) REFERENCES user(userID) on update cascade on delete cascade,
    foreign key (prepBy) REFERENCES user(userID) on update cascade on delete cascade
);


CREATE table VoucherDetails(
    vouchID VARCHAR(5) NOT NULL ,
    sourceNo INT, 
    Amount DECIMAL(10,2), 
    Narration VARCHAR(100),

    primary key(vouchID),
    foreign key (vouchID) REFERENCES Voucher(vouchID) on update cascade on delete cascade
    
);


CREATE table CreditVoucher (
    vouchID VARCHAR(5) NOT NULL, 
    vDATE DATE, 
    credit DECIMAL(10,2), 
    authBy VARCHAR(100), 
    prepBy VARCHAR(100),

    PRIMARY KEY(vouchID),
    FOREIGN KEY(vouchID) REFERENCES Voucher(vouchID),
    FOREIGN KEY(authBy) REFERENCES User(userID),
    FOREIGN KEY(prepBy) REFERENCES User(userID)
);


CREATE table DebitVoucher ( 
    vouchID VARCHAR(5) NOT NULL, 
    vDATE DATE, 
    debit DECIMAL(10,2), 
    authBy VARCHAR(100), 
    prepBy VARCHAR(100),
    PRIMARY KEY(vouchID),
    FOREIGN KEY(vouchID) REFERENCES Voucher(vouchID)
);

CREATE table Credit (
    vouchID VARCHAR(5) NOT NULL, 
    accountID VARCHAR(5) NOT NULL, 
    sourceNo INT,     
    Amount DECIMAL(10,2), 
    Narration VARCHAR(100),

    PRIMARY KEY(vouchID),
    FOREIGN KEY(vouchID) REFERENCES Voucher(vouchID),
    FOREIGN KEY(accountID) REFERENCES Account(accountID)
);

CREATE table Debit(
    vouchID VARCHAR(5) NOT NULL, 
    accountID VARCHAR(5) NOT NULL, 
    sourceNo INT, 
    Amount DECIMAL(10,2), 
    Narration VARCHAR(100),

    PRIMARY KEY(vouchID),
    FOREIGN KEY(vouchID) REFERENCES Voucher(vouchID),
    FOREIGN KEY(accountID) REFERENCES Account(accountID)
);


CREATE table SupportDoc(
    vouchID VARCHAR(5) NOT NULL,
    sourceNo INT NOT NULL UNIQUE, 
    docName VARCHAR(100), 
    docDATE DATE,

    CONSTRAINT supDocID PRIMARY KEY(vouchID, sourceNo),
    FOREIGN KEY(vouchID) REFERENCES Voucher(vouchID)
    ON DELETE CASCADE
    ON UPDATE CASCADE 

);

*/

CREATE table Customer(
    custID VARCHAR(10) NOT NULL, 
    fname VARCHAR(100), 
    lname VARCHAR(100), 
    trn INT, 
    email VARCHAR(255), 

    PRIMARY KEY(custID)
);


CREATE table Invoice(
    invoiceID VARCHAR(10) NOT NULL, 
    custID VARCHAR(10), 
    invoice_DATE DATE, 
    tax_tot DECIMAL(10,2),

    PRIMARY KEY(invoiceID),
    FOREIGN KEY(custID) REFERENCES Customer(custID)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);


CREATE TABLE `Order`(
    orderID VARCHAR(10) NOT NULL, 
    order_tot DECIMAL(10,2), 
    order_DATE DATE, 
    custID VARCHAR(10), 
    invoiceID VARCHAR(10), 
    busID INT(10) ,
    status VARCHAR(20),

    PRIMARY KEY(orderID),
    FOREIGN KEY(custID) REFERENCES Customer(custID)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
    FOREIGN KEY(invoiceID) REFERENCES Invoice(custID)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
    FOREIGN KEY(busID) REFERENCES Business(busID)
    ON UPDATE CASCADE
    ON DELETE CASCADE

);


CREATE table OrderDetails(
    orderID VARCHAR(10), 
    detailsID VARCHAR(10), 
    prodID VARCHAR(10), 
    serviceID VARCHAR(10), 
    quantity INT, 
    order_tot DECIMAL(10,2),

    CONSTRAINT PK_Value PRIMARY KEY(orderID, detailsID),
    FOREIGN KEY(orderID) REFERENCES `Order`(orderID)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);
    

CREATE table Asset(
    asset_id VARCHAR(10), 
    a_name VARCHAR(100), 
    lifeSpan INT, 
    a_type VARCHAR(100), 
    acquisDATE DATE, 
    a_value DECIMAL(10.2), 
    busID INT(10) ,

    PRIMARY KEY(asset_id),
    FOREIGN KEY(busID) REFERENCES Business(busID)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

CREATE table CurrentAsset(
    asset_id VARCHAR(10), 
    a_name VARCHAR(100), 
    lifeSpan INT, 
    a_type VARCHAR(100), 
    acquisDATE DATE, 
    a_value DECIMAL(10,2), 
    ca_id VARCHAR(10) NOT NULL, 
    busID INT(10) ,

    PRIMARY KEY(ca_id),
    FOREIGN KEY(asset_id) REFERENCES Asset(asset_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
    FOREIGN KEY(busID) REFERENCES Business(busID)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

CREATE table NonCurrentAsset(
    asset_id VARCHAR(10), 
    a_name VARCHAR(100), 
    lifeSpan INT, 
    a_type VARCHAR(100), 
    acquisDATE DATE, 
    a_value DECIMAL(10,2), 
    nca_id VARCHAR(10) NOT NULL, 
    AccumDep DECIMAL(10,2), 
    disposalAmt DECIMAL(10,2), 
    depType VARCHAR(100), 
    busID INT(10),

    PRIMARY KEY(nca_id),
    FOREIGN KEY(asset_id) REFERENCES Asset(asset_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
    FOREIGN KEY(busID) REFERENCES Business(busID)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);


CREATE table Liability(
    liab_id VARCHAR(5) NOT NULL unique , 
    liab_type VARCHAR(100), 
    liab_name VARCHAR(100), 
    Amt_owed DECIMAL(10,2), 
    borw_DATE DATE, 
    loan_period INT, 
    busID INT(10),

    PRIMARY KEY(liab_id),
    FOREIGN KEY(busID) REFERENCES Business(busID)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);
    
CREATE table currentLiability(
    liab_id VARCHAR(10),
    cliab_id VARCHAR(10) NOT NULL unique, 
    liab_type VARCHAR(100), 
    liab_name VARCHAR(100), 
    Amt_owed DECIMAL(10,2), 
    borw_DATE DATE, 
    loan_period INT, 
    busID INT(10),
    PRIMARY KEY(cliab_id),
    FOREIGN KEY(liab_id) REFERENCES Liability(liab_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
    FOREIGN KEY(busID) REFERENCES Business(busID)
    ON DELETE CASCADE
    ON UPDATE CASCADE 
);

CREATE table longTermLiability(
    liab_id VARCHAR(10),
    Itliab_id VARCHAR(10) NOT NULL unique, 
    liab_type VARCHAR(100), 
    liab_name VARCHAR(100), 
    Amt_owed DECIMAL(10,2), 
    borw_DATE DATE, 
    loan_period INT, 
    busID INT(10),

    PRIMARY KEY(Itliab_id),
    FOREIGN KEY(liab_id) REFERENCES Liability(liab_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
    FOREIGN KEY(busID) REFERENCES Business(busID)
    ON DELETE CASCADE
    ON UPDATE CASCADE 
);

CREATE table Expense(
    expenseID VARCHAR(10) NOT NULL unique, 
    extype VARCHAR(100), 
    exname VARCHAR(100), 
    dateIncurred DATE, 
    expenseAmt DECIMAL(10,2),
    
    PRIMARY KEY(expenseID)
);

CREATE table Purchase(
    purchaseID VARCHAR(10) NOT NULL unique, 
    p_date DATE, 
    p_item VARCHAR(100), 
    p_quantity INT, 
    p_price DECIMAL(10,2), 
    busID INT(10), 
    stmtID VARCHAR(10),

    PRIMARY KEY(purchaseID),
    FOREIGN KEY(busID) REFERENCES Business(busID),
    FOREIGN KEY(stmtID) REFERENCES FinancialStmt(stmtID)
);


CREATE TABLE  Product  (
   prodID  VARCHAR(10) NOT NULL,
   prodName  VARCHAR(100) ,
   unit_price  DECIMAL(10,2),
   baseUnit  DECIMAL(10,2),
   limitedTime  DATETIME,
   taxPercent  DECIMAL(3,2),
   prodStatus  VARCHAR(25),

   PRIMARY KEY(prodID)

);

CREATE table stock(
    prodID VARCHAR(10), 
    inStock VARCHAR(10), 
    lastUpdateTime DATETIME, 
    quantity INT(11),
    threshold INT(11),
    PRIMARY KEY(prodID),
    FOREIGN KEY(prodID) REFERENCES Product(prodID)
    ON DELETE CASCADE
    ON UPDATE CASCADE
    
);
CREATE table Receipt(
    receiptID VARCHAR(10) NOT NULL, 
    orderID VARCHAR(10),
    busID INT(10), 
    date_issued DATE,

    PRIMARY KEY(receiptID),
    FOREIGN KEY(busID) REFERENCES Business(busID)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
    FOREIGN KEY(orderID) REFERENCES `Order`(orderID)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);


CREATE table Service(
    serviceID VARCHAR(11) NOT NULL, 
    serv_name VARCHAR(11) , 
    serv_price INT(11) , 
    taxPercent DECIMAL(3,2) , 
    in_season VARCHAR(11) , 
    
    PRIMARY KEY(serviceID)
    
); 


CREATE table service_sale_item(
    ssiID VARCHAR(11) , 
    serv_price INT(11) , 
    taxAmt INT(11) , 
    serviceID VARCHAR(11), 
    userID VARCHAR(5),

    PRIMARY KEY(ssiID),
    FOREIGN KEY(ssiID) REFERENCES Service(serviceID)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
    FOREIGN KEY(userID) REFERENCES User(userID)
    ON DELETE CASCADE
    ON UPDATE CASCADE
        
);

CREATE table ReceiptDetails(
    receiptID VARCHAR(10) NOT NULL unique, 
    rdetailsID VARCHAR(10), 
    orderID VARCHAR(10), 
    prodID VARCHAR(10), 
    serviceID VARCHAR(10), 
    quantity INT, 
    order_tot DECIMAL(10,2),

    PRIMARY KEY(rdetailsID),
    FOREIGN KEY(receiptID) REFERENCES Receipt(receiptID)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
    FOREIGN KEY(orderID) REFERENCES `Order`(orderID)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
    FOREIGN KEY(prodID) REFERENCES Product(prodID)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
    FOREIGN KEY(serviceID) REFERENCES Service(serviceID)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

CREATE table Sale(
    saleID VARCHAR(11) NOT NULL, 
    customerID VARCHAR(11), 
    timePaid DATETIME, 
    timeCreated DATETIME, 
    saleAmt INT(11), 
    saleAmtPaid INT(11), 
    SaleStatus VARCHAR(11), 
    receiptID VARCHAR(11),

    PRIMARY KEY(saleID),
    FOREIGN KEY(customerID) REFERENCES Customer(custID)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
    FOREIGN KEY(receiptID) REFERENCES Receipt(receiptID)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);


CREATE table con_service_sale_item(
    cssiID VARCHAR(11) NOT NULL, 
    quantitySold INT(11), 
    unit_price INT(11), 
    serv_price INT(11), 
    taxAmt INT(11), 
    serviceID VARCHAR(11), 
    starttime DATETIME , 
    endtime DATETIME , 
    prolong_period DATETIME ,

    PRIMARY KEY(cssiID),
    FOREIGN KEY(serviceID) REFERENCES Service(serviceID)
    ON DELETE CASCADE
    ON UPDATE CASCADE

);

CREATE table Con_Service(
    serviceID VARCHAR(11) NOT NULL , 
    serv_name VARCHAR(11) , 
    serv_uprice INT(11) , 
    basic_unit DECIMAL(10,2) , 
    d_prolongperiod DATETIME , 
    taxPercent DECIMAL(3,2), 
    in_season VARCHAR(11) , 
    cssiID VARCHAR(11),

    PRIMARY KEY(serviceID),
    FOREIGN KEY(cssiID) REFERENCES con_service_sale_item(cssiID)
    ON DELETE CASCADE
    ON UPDATE CASCADE
    
);


CREATE table product_sale_item(
    psiID INT(11) NOT NULL, 
    customerID VARCHAR(11), 
    timePaid DATETIME , 
    timeCreated DATETIME, 
    saleAmt DECIMAL(10,2) , 
    saleAmtPaid DECIMAL(10,2),  
    SaleStatus VARCHAR(25), 
    quantitySold DECIMAL(10,2), 
    unit_price DECIMAL(10, 2), 
    prodID VARCHAR(25), 
    taxAmt DECIMAL(10, 2), 

    PRIMARY KEY(psiID),
    FOREIGN KEY(customerID) REFERENCES Customer(custID)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
    FOREIGN KEY(prodID) REFERENCES Product(prodID)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

