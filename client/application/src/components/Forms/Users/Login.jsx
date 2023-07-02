import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { Link } from "react-router-dom";
import { Alert } from "react-bootstrap";

import {useFormik} from "formik";
import * as Yup from "yup";

import { login } from "../../../auth.js";
import Logo from "../../../images/logo.png"
import LoadingPage from "../../Misc/LoadingPage"

import 'bootstrap/dist/css/bootstrap.css';
import "./Login.css"



export default function LoginPage(props){

    const { title } = props;

    const navigate = useNavigate();

    const [state, setState] = useState({
        title : `Login - ${title}`,
        serverResponse : {},
        showAlert : false
    });

    useEffect(() => {
        document.title = state.title;
    }, [state.title]);

    const formik = useFormik({
        initialValues : {
            username : "",
            password : ""
        },

        validationSchema : Yup.object({
            username : Yup.string().required("username is required"),
            password : Yup.string().required("password is required")
                        // .matches(/[a-z]/g, "Should contain at least 1 lowercase")
                        // .matches(/[A-Z]/g, "Should contain at least 1 uppercase")
                        // .matches(/[0-9]/g, "Should contain at least 1 numeric")
                        .matches(/^\S*$/, "Should not contain spaces")
            
        }),
        onSubmit : (data, { setSubmitting }) => {
            setSubmitting(true)
            const body  = {
                username : data.username,
                password : data.password
            };

            const requestOption = {
                method : "POST",
                headers : {
                    "content-type" : "application/json"
                },
                body : JSON.stringify(body)
            }
            
            fetch("/login", requestOption)
                .then(response => response.json())
                .then(data => {
                    console.log(data);
                    setState({
                        ...state,
                        serverResponse : {
                            status : data.login
                        }
                    });
                    if (data.login){
                        login(data.access_token);
                        navigate(`/`);
                    } else {
                        setState({
                            ...state,
                            showAlert :true
                        });
                    }
                    
                })
                .catch(error => {
                    console.error(error);
                })
                .finally( () => {
                    setSubmitting(false);
                })
        }
    })

    return (
        <div>
            <main className="d-flex justify-content-center align-items-center form-signin">
                <form onSubmit={formik.handleSubmit}>
                    <img className="mb-4" src={Logo} alt="" height="100" />
                    <h1 className="h3 mb-3 fw-normal">Please sign in</h1>

                    {state.showAlert ? 
                        <Alert variant="danger">
                            Failed to login, please try again
                        </Alert> : ""}

                    <div className="form-floating">
                        <input type="username" 
                            className="form-control"
                            name="username" 
                            id="floatingInput" 
                            placeholder="Username"
                            value={formik.values.username}
                            onChange={formik.handleChange}
                            onBlur={formik.handleBlur} 
                        />
                        <label htmlFor="floatingInput">Username</label>
                    </div>
                    <div className="form-floating">
                        <input type="password" 
                            className="form-control"
                            name="password"
                            id="floatingPassword" 
                            placeholder="Password"
                            value={formik.values.password}
                            onChange={formik.handleChange}
                            onBlur={formik.handleBlur}  
                        />
                        <label htmlFor="floatingPassword">Password</label>
                    </div>
                    <button className="btn btn-primary w-100 py-2" type="submit">Sign in</button>
                    <div className="form-group my-3">
                        <small>Do not have an account? <Link className="text-decoration-none" to={`/signup`}>Sign up</Link></small>
                    </div>
                    <p className="mt-5 mb-3 text-body-secondary">&copy; 2023</p>
                </form>
            </main>
            {formik.isSubmitting ? (<LoadingPage />) : ""}
        </div>
        
    );
}