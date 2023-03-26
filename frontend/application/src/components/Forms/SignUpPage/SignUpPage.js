import React from "react";
import {useFormik} from "formik";
import * as Yup from "yup";

import "./SignUpPage.css";

function SignUpPage(){

    const formik = useFormik({
        initialValues : {
            username : "",
            email : "",
            password : "",
            confirmPassword : "",
            secretCode : "",
            agreement : false
        },

        validationSchema : Yup.object({
            username : Yup.string().required().min(4),
            email : Yup.string().required().email(),
            password : Yup.string().required().min(8)
                        .matches(/[a-z]/g, "Should contain at least 1 lowercase")
                        .matches(/[A-Z]/g, "Should contain at least 1 uppercase")
                        .matches(/[0-9]/g, "Should contain at least 1 numeric")
                        .matches(/^\S*$/, "Should not contain spaces"),
            confirmPassword : Yup.string().required()
                                .oneOf([Yup.ref("password")], "Password must match"),
            secretCode : Yup.string().required(),
            agreement : Yup.boolean().isTrue()
            
        }),

        onSubmit : (values) => {
            setTimeout(()=>{
                formik.setSubmitting(false);
                formik.resetForm();
            }, 2000);
            
        }
    });

    return (
        <section className="page--signup">

            <div className="main--box--signup">

                <h1 className="title--page--signup">
                    Register New Account
                </h1>

                <form className="form--signup" onSubmit={formik.handleSubmit}>
                    <div className="form--group--signup">
                        <label className="label--form--signup">Username</label>
                        <input  className="input--form-signup"
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

                    <div className="form--group--signup">
                        <label className="label--form--signup">Email</label>
                        <input  className="input--form-signup" 
                                name="email" 
                                type="email"
                                value={formik.values.email}
                                onChange={formik.handleChange}
                                onBlur={formik.handleBlur}  />

                        <div className="error">
                            <small>
                                {(formik.errors.email && formik.touched.email) ? formik.errors.email : ""}
                            </small>
                        </div>
                    </div>

                    <div className="form--group--signup">
                        <label className="label--form--signup">Password</label>
                        <input  className="input--form-signup" 
                                name="password" 
                                type="password"
                                value={formik.values.password}
                                onChange={formik.handleChange}
                                onBlur={formik.handleBlur}  />
                        <div className="error">
                            <small>
                                {(formik.errors.password && formik.touched.password ) ? formik.errors.password : ""}
                            </small>
                        </div>
                    </div>

                    <div className="form--group--signup">
                        <label className="label--form--signup">Confirm Password</label>
                        <input  className="input--form-signup" 
                                name="confirmPassword" 
                                type="password"
                                value={formik.values.confirmPassword}
                                onChange={formik.handleChange}
                                onBlur={formik.handleBlur}  />
                        <div className="error">
                            <small>
                                {(formik.errors.confirmPassword && formik.touched.confirmPassword )? formik.errors.confirmPassword : ""}
                            </small>
                        </div>
                    </div>

                    <div className="form--group--signup">
                        <label className="label--form--signup">Secret Code</label>
                        <input  className="input--form-signup" 
                                name="secretCode"
                                type="password"
                                value={formik.values.secretCode}
                                onChange={formik.handleChange}
                                onBlur={formik.handleBlur}  />

                        <div className="error">
                            <small>
                                {(formik.errors.secretCode && formik.touched.secretCode)? formik.errors.secretCode : ""}
                            </small>
                        </div>
                    </div>

                    <div className="form--group--signup form--checkbox--signup">
                        <input  type="checkbox" 
                                name="agreement"
                                checked={formik.values.agreement}
                                onChange={formik.handleChange}
                                onBlur={formik.handleBlur}  />
                        <label className="checkbox--signup">I agree to Terms of Services.</label>
                    </div> 
                    <div className="error">
                        <small>
                            {(formik.errors.agreement && formik.touched.agreement)? formik.errors.agreement : ""}
                        </small>
                    </div>                   
                    
                    <input className="submit--form-signup" 
                            type="submit"
                            value="Register"
                            disabled={formik.isSubmitting} />
                </form>
                
            </div>
            <small>
                    Already has an account? <span className="login--text--anchor--signup">Login here.</span>
            </small>
        </section>
    )
}

export default SignUpPage;