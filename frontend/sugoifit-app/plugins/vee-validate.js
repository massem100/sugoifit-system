import { extend } from "vee-validate";
import { required,email } from "vee-validate/dist/rules";
extend("required", {
  ...required,
  message: "This {_field_} is required"
});
extend("email", {
  ...email,
  message: "Email format not correct"
});
extend('password', {
  params: ['target'],
  validate(value, { target }) {
    return value === target;
  },
  message: 'Password does not match'
});
extend('max', {
   validate(value, args) {
    const length = value.length;

    return  length <= args.max;
  },
  params: ['max'],
  message: 'The {_field_} should not greater than {max} digits'
});
