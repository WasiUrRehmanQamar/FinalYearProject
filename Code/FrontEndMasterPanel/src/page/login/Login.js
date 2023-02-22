import React, { useEffect, useState } from 'react'
import './login.css'
import { Link } from 'react-router-dom'
const Login = () => {

  return (
    <>

      <>
        <div class="circle"></div>
        <div className='form-design'>
          <div class="form_div">
            {/* <h2 class="form__title">My Malqiyet</h2> */}
            <img className='form_logo' />
            <p class="form__paragraph">You do not have an account yet?</p>
            <div class="form__container">
              <div class="form__group">
                <input type="text" id="name" class="form__input" placeholder=" " />
                <label for="name" class="form__label" >Username:</label>
                <span class="form__line"></span>
              </div>
              <div class="form__group">
                <input type="password" id="user" class="form__input" placeholder=" " />
                <label for="user" class="form__label">Password:</label>
                <span class="form__line"></span>
              </div>

              <Link to={"/Dashboard"} class="form__submit">Login</Link>
            </div>
          </div>
        </div>
      </>


    </>
  )
}

export default Login