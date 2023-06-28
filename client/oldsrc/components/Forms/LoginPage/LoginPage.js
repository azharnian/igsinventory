import React from "react";
import { useFormik } from "formik"; 
import * as Yup from "yup";

import LoadingPage from "../../ContentPage/LoadingPage/LoadingPage";

import "./LoginPage.css"
import logo from "./images/logo.svg"

function LoginPage(){

    const formik = useFormik({
        initialValues : {
            username : "",
            password : ""
        },

        validationSchema : Yup.object({
            username : Yup.string().required(),
            password : Yup.string().required()
        }),

        onSubmit : values => {
            setTimeout(()=>{
                formik.setSubmitting(false);
            }, 2000);
        }
    })

    return (
        <section className="page--login">

            <div className="main--box--login">

                <img className="logo--login" src={logo} alt="logo login" />

                <form className="form--login" onSubmit={formik.handleSubmit}>

                    <div className="form--group--login">
                        <label className="label--form--login">Username</label>
                        <input className="input--form-login" 
                                name="username" 
                                type="text"
                                value={formik.values.username}
                                onChange={formik.handleChange}
                                onBlur={formik.handleBlur} 
                                autoFocus />

                        <div className="error">
                            <small>
                                {(formik.errors.username && formik.touched.username) ? formik.errors.username : ""}
                            </small>
                        </div>
                    </div>

                    <div className="form--group--login">
                        <label className="label--form--login">Password</label>
                        <input className="input--form-login" 
                                name="password" 
                                type="password"
                                value={formik.values.password}
                                onChange={formik.handleChange}
                                onBlur={formik.handleBlur} />

                        <div className="error">
                            <small>
                                {(formik.errors.password && formik.touched.password) ? formik.errors.password : ""}
                            </small>
                        </div>
                    </div>


                    <input className="submit--form--login" 
                            type="submit" 
                            value="Log In"
                            disabled={formik.isSubmitting} />
                </form>

                <hr />
                <small>
                    Don't have an account? <span className="login--text--anchor--login">Register here.</span>
                </small>
            </div>
            {formik.isSubmitting ? (<LoadingPage />) : ""}
        </section>
    )
}

export default LoginPage;