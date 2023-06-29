import React from "react";

import 'bootstrap/dist/css/bootstrap.css';
import "./Login.css"


export default function Login(){

    return (
        <div>
            <main className="d-flex justify-content-center align-items-center form-signin">
                <form>
                    <img className="mb-4" alt="" width="72" height="57" />
                    <h1 className="h3 mb-3 fw-normal">Please sign in</h1>

                    <div className="form-floating">
                    <input type="text" className="form-control" id="floatingInput" placeholder="Username" />
                    <label htmlFor="floatingInput">Username</label>
                    </div>
                    <div className="form-floating">
                    <input type="password" className="form-control" id="floatingPassword" placeholder="Password" />
                    <label htmlFor="floatingPassword">Password</label>
                    </div>
                    <button className="btn btn-primary w-100 py-2" type="submit">Sign in</button>
                    <p className="mt-5 mb-3 text-body-secondary">&copy; 2023</p>
                </form>
            </main>
        </div>
        
    );
}