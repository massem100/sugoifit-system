import {userService} from '../services'

export default function ({ app: { $axios } }, inject) {

    
    //  create an instance of the userService with the prefix 'My App'
    const userServ = new userService($axios);
    
  
    // Will be available in the components as this.$myService
    inject('userService', userServ);
  
  }