import React from 'react';
import classes from './Checkout.module.css';
import { useRef, useState} from 'react';

const isEmpty=value=>value.trim()==='';
const isPhoneNumber=value=>value.trim().length===9;

const Checkout = (props) => {
    const [formInputsValidity, setFormInputsValidity]=useState({
        name: true, 
        phone: true, 
        email: true, 
        address: true
    });

    const nameInputRef=useRef();
    const phoneInputRef=useRef();
    const emailInputRef=useRef();
    const addressInputRef=useRef();

  const confirmHandler = (event) => {
    event.preventDefault();

    const enteredName=nameInputRef.current.value;
    const enteredPhone=phoneInputRef.current.value;
    const enteredEmail=emailInputRef.current.value;
    const enteredAddress=addressInputRef.current.value;

    const enteredNameIsValid=!isEmpty(enteredName);
    const enteredPhoneIsValid=isPhoneNumber(enteredPhone);
    const enteredEmailIsValid=!isEmpty(enteredEmail);
    const enteredAddressIsValid=!isEmpty(enteredAddress);

    setFormInputsValidity({
        name: enteredNameIsValid, 
        phone: enteredPhoneIsValid, 
        email: enteredEmailIsValid, 
        address: enteredAddressIsValid
    });

    const formIsValid=enteredNameIsValid&&enteredPhoneIsValid&&enteredEmailIsValid&&enteredAddressIsValid;

    if(!formIsValid){
        return
    }

    props.onConfirm({
      name: enteredName, 
      phone: enteredPhone, 
      email: enteredEmail, 
      address: enteredAddress
    });

  };

  return (
    <form className={classes.form} onSubmit={confirmHandler}>
      <div className={`${classes.control} ${formInputsValidity.name?'':classes.invalid}`}>
        <label htmlFor='name'>Full Name</label>
        <input type='text' id='name' ref={nameInputRef}/>
        {!formInputsValidity.name&&<p>Please enter a valid name!</p>}
      </div>
      <div className={`${classes.control} ${formInputsValidity.phone?'':classes.invalid}`}>
        <label htmlFor='phone'>Phone</label>
        <input type='text' id='phone' ref={phoneInputRef} />
        {!formInputsValidity.phone&&<p>Please enter a valid phone number!</p>}
      </div>
      <div className={`${classes.control} ${formInputsValidity.email?'':classes.invalid}`}>
        <label htmlFor='email'>Email</label>
        <input type='email' id='email' ref={emailInputRef}/>
        {!formInputsValidity.email&&<p>Please enter a valid email!</p>}
      </div>
      <div className={`${classes.control} ${formInputsValidity.address?'':classes.invalid}`}>
        <label htmlFor='address'>Address</label>
        <input type='text' id='address' ref={addressInputRef}/>
        {!formInputsValidity.address&&<p>Please enter a valid address!</p>}
      </div>
      <div className={classes.actions}>
        <button type='button' onClick={props.onCancel}>
          Cancel
        </button>
        <button className={classes.submit}>Confirm</button>
      </div>
    </form>
  );
};

export default Checkout;