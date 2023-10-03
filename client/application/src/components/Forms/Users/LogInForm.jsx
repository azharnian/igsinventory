import { Link } from "react-router-dom";

import { useFormik } from "formik";
import * as Yup from "yup";

import "bootstrap/dist/css/bootstrap.css"
import "./css/LogIn.css"

export default function LogInForm(){
    
    const formik = useFormik({
        initialValues : {
            username : "",
            password : ""
        },

        validationSchema : Yup.object({
            username : Yup.string().required("username is required"),
            password : Yup.string().required("password is required")
            
        })
    })

    return (
        <>
            <main className="d-flex justify-content-center align-items-center form-signin">
                <form onSubmit={formik.handleSubmit}>
                    <img className="mb-4" src={""} alt="" height="100" />
                    <h1 className="h3 mb-3 fw-normal">Please sign in</h1>


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
            {formik.isSubmitting ? (<>Loading</>) : ""}
        </>  
    );
}