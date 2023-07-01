import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";

import {Button, Modal} from "react-bootstrap";
import {useFormik} from "formik";
import * as Yup from "yup";

import Logo from "../../../images/logo.png"
import LoadingPage from "../../Misc/LoadingPage";
import "./Signup.css"

export default function SignupPage(){

    const navigate = useNavigate();

    const [state, setState] = useState({
        serverResponse : {},
        showModal : false
    })

    // No longer used, already had formik
    function handleInputChange(e) {
        const {name, value} = e.target
        setState({
            ...state,
            [name] : value
        })
    }

    // No longer used, already had formik
    function handleSubmitForm(data) {
        // e.preventDefault();
        console.log(data);
    }

    const formik = useFormik({
        initialValues : {
            firstName : "",
            lastName : "",
            username : "",
            email : "",
            phone : "",
            password : "",
            confirmPassword : "",
            agreed : true
        },

        validationSchema : Yup.object({
            firstName : Yup.string().required("firstname is required").max(128),
            lastName : Yup.string().required("lastname is required").max(128),
            username : Yup.string().required("username is required").min(4),
            email : Yup.string().required("email is required").email(),
            phone : Yup.string().required("phone is required").min(8),
            password : Yup.string().required().min(8)
                        // .matches(/[a-z]/g, "Should contain at least 1 lowercase")
                        // .matches(/[A-Z]/g, "Should contain at least 1 uppercase")
                        // .matches(/[0-9]/g, "Should contain at least 1 numeric")
                        .matches(/^\S*$/, "Should not contain spaces"),
            confirmPassword : Yup.string().required()
                                .oneOf([Yup.ref("password")], "Password must match"),
            agreed : Yup.boolean().isTrue("must agree")
            
        }),

        onSubmit : (data, { setSubmitting }) => {
            setSubmitting(true)
            const body  = {
                username : data.username,
                email : data.email,
                phone : data.phone,
                password : data.password,
                first_name : data.firstName,
                last_name : data.lastName
            };

            const requestOption = {
                method : "POST",
                headers : {
                    "content-type" : "application/json"
                },
                body : JSON.stringify(body)
            }
            
            fetch("/signup", requestOption)
                .then(response => response.json())
                .then(data => {
                    // console.log(data);
                    setState({
                        ...state,
                        serverResponse : {
                            status : data.added.status,
                            orig : data.added.orig
                        },
                        showModal : true
                    });
                })
                .catch(error => {
                    console.error(error);
                })
                .finally( () => {
                    setSubmitting(false);
                })
        }
            
        });

    return (
        <div className="container">
            <main>
                <div className="py-5 text-center">
                <img className="d-block mx-auto mb-4" src={Logo} alt="" height="57"/ >
                <h2>Registration</h2>
                <p className="lead"></p>
                </div>

                <div className="row d-flex justify-content-center">
                
                    <div className="col-md-9 col-lg-10">
                        <h4 className="mb-3">User Information</h4>
                        <form className="needs-validation" onSubmit={formik.handleSubmit}>
                            <div className="row g-3">
                                <div className="col-sm-6">

                                    <label htmlFor="firstName" className="form-label">First name</label>
                                    <input type="text" 
                                        className="form-control" 
                                        id="firstName"
                                        name="firstName" 
                                        placeholder="" 
                                        value={formik.values.firstName}
                                        onChange={formik.handleChange}
                                        onBlur={formik.handleBlur}
                                        />

                                    <small style={{color : "red"}}> 
                                        {(formik.errors.firstName && formik.touched.firstName) ? formik.errors.firstName : ""}
                                    </small>
                                </div>

                                <div className="col-sm-6">
                                    <label htmlFor="lastName" className="form-label">Last name</label>
                                    <input type="text" 
                                        className="form-control" 
                                        id="lastName"
                                        name="lastName" 
                                        placeholder=""
                                        onChange={formik.handleChange} 
                                        onBlur={formik.handleBlur}
                                        />
                                    <small style={{color : "red"}}> 
                                        {(formik.errors.lastName && formik.touched.lastName) ? formik.errors.lastName : ""}
                                    </small>
                                </div>

                                <div className="col-12">
                                    <label htmlFor="username" className="form-label">Username</label>
                                    <div className="input-group has-validation">
                                        <span className="input-group-text">@</span>
                                        <input type="text" 
                                        className="form-control" 
                                        id="username"
                                        name="username" 
                                        placeholder=""
                                        onChange={formik.handleChange}
                                        onBlur={formik.handleBlur}
                                        />
                                    </div>
                                    <small style={{color : "red"}}> 
                                        {(formik.errors.username && formik.touched.username) ? formik.errors.username : ""}
                                    </small>
                                </div>

                                <div className="col-12">
                                    <label htmlFor="email" className="form-label">Email</label>
                                    <input type="email" 
                                        className="form-control" 
                                        id="email" 
                                        name="email"
                                        placeholder="you@example.com"
                                        onChange={formik.handleChange}
                                        onBlur={formik.handleBlur}
                                        />
                                    <small style={{color : "red"}}> 
                                        {(formik.errors.email && formik.touched.email) ? formik.errors.email : ""}
                                    </small>
                                </div>

                                <div className="col-12">
                                    <label htmlFor="phone" className="form-label">Phone</label>
                                    <input type="phone" 
                                        className="form-control" 
                                        id="phone"
                                        name="phone" 
                                        placeholder="08xxxxxx"
                                        onChange={formik.handleChange}
                                        onBlur={formik.handleBlur}
                                        />
                                    <small style={{color : "red"}}> 
                                        {(formik.errors.phone && formik.touched.phone) ? formik.errors.phone : ""}
                                    </small>
                                </div>

                            
                                <div className="col-md-6">
                                    <label htmlFor="password" className="form-label">Password</label>
                                    <input type="password" 
                                        className="form-control" 
                                        id="password"
                                        name="password" 
                                        placeholder=""
                                        onChange={formik.handleChange}
                                        onBlur={formik.handleBlur}
                                        />
                                    <small style={{color : "red"}}> 
                                        {(formik.errors.password && formik.touched.password) ? formik.errors.password : ""}
                                    </small>
                                </div>

                                <div className="col-md-6">
                                    <label htmlFor="confirmPassword" className="form-label">Confirm Password</label>
                                    <input type="password" 
                                        className="form-control" 
                                        id="confirmPassword" 
                                        name="confirmPassword"
                                        placeholder=""
                                        onChange={formik.handleChange}
                                        onBlur={formik.handleBlur}
                                        />
                                    <small style={{color : "red"}}> 
                                        {(formik.errors.confirmPassword && formik.touched.confirmPassword) ? formik.errors.confirmPassword : ""}
                                    </small>
                                
                                </div>

                                
                            </div>

                            <hr className="my-4" />

                            <div className="form-check">
                                <div className="form-group" >
                                    <input type="checkbox" 
                                        className="form-check-input" 
                                        id="agreed"
                                        name="agreed"
                                        onChange={formik.handleChange}
                                        onBlur={formik.handleBlur}
                                        />
                                    <label htmlFor="agreed" className="form-check-label">I agree with all terms and conditions applied.</label>
                                </div>
                                
                                <small style={{color : "red"}}> 
                                    {(formik.errors.agreed && formik.touched.agreed) ? formik.errors.agreed : ""}
                                </small>
                            </div>


                            <hr className="my-4" />

                            <button className="w-100 btn btn-primary btn-lg" 
                            type="submit"
                            disabled={formik.isSubmitting}
                            >Sign Up</button>
                            <div className="form-group my-3">
                                <small>
                                Already has an account, login
                                <span className="mx-1">
                                    <Link className="text-decoration-none" to={`/login`}>here</Link>
                                </span> 
                                </small>
                            </div>
                        </form>
                    </div>
                
                </div>
            </main>
            {formik.isSubmitting ? (<LoadingPage />) : ""}
            {state.showModal ? (
                <Modal centered show={state.showModal} onHide={() => setState({
                    ...state,
                    showModal : false
                    })}>
                    <Modal.Header className={`bg-${state.serverResponse.status === "failed" ? "danger" : "success"} text-white`} closeButton>
                        <Modal.Title className="text-uppercase">{state.serverResponse.status}</Modal.Title>
                    </Modal.Header>
                    <Modal.Body>
                        <p>{state.serverResponse.orig}</p>
                    </Modal.Body>
                    <Modal.Footer>
                        {state.serverResponse.orig ? 
                        <Button variant="primary" onClick={() => setState({
                                                                ...state,
                                                                showModal : false
                                                                })}>
                        Close
                        </Button> :
                        <Button variant="primary" onClick={() => navigate(`/login`)}>
                        Login
                        </Button>
                        }
                    </Modal.Footer>
                </Modal>
            ) : ""}
        </div>
    );
}