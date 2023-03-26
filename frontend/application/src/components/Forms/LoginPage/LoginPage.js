import React from "react";
import "./LoginPage.css"
import logo from "./images/logo.svg"

function LoginPage(){

    return (
        <section className="page--login">

            <div className="main--box--login">

                <img className="logo--login" src={logo} alt="logo login" />

                <form className="form--login">

                    <div className="form--group--login">
                        <label className="label--form--login">Username</label>
                        <input className="input--form-login" name="Username" type="text" autoFocus />
                    </div>

                    <div className="form--group--login">
                        <label className="label--form--login">Password</label>
                        <input className="input--form-login" name="Password" type="password" />
                    </div>

                    <div className="form--checkbox--login">
                        <input type="checkbox" />
                        <label className="checkbox--login">Remember me</label>
                    </div>

                    <input className="submit--form-login" type="submit" value="Log In"/>
                </form>

                <hr />
                <small>
                    Don't have an account? <span className="login--text--anchor--login">Register here.</span>
                </small>
            </div>

        </section>
    )
}

export default LoginPage;