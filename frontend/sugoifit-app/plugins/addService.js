import {userService} from '../services'
import {productService} from '../services/product.service'

export default function ({ app: { $axios } }, inject) {

    
    //  create an instance of the userService with the prefix 'My App'
    const userServ = new userService($axios);
    const prodServ = new productService($axios);
    
    
    // Will be available in the components as this.$myService
    inject('userService', userServ);
    inject('productService', prodServ);
  
  }