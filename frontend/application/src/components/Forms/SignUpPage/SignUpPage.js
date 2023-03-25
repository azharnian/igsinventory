import "./SignUpPage.css"

function SignUpPage(){

    return (
        <section className="page--sign--up">

            <div className="main--box--sign--up">

                <h1>
                    Register New Account
                </h1>

                <form className="form--sign--up">

                    <label className="label--form--sign--up">Username</label>
                    <input className="input--form-sign--up" name="Username" type="text" autoFocus/>

                    <label className="label--form--sign--up">Email</label>
                    <input className="input--form-sign--up" name="Email" type="email" />

                    <label className="label--form--sign--up">Password</label>
                    <input className="input--form-sign--up" name="Password" type="password" />

                    <label className="label--form--sign--up">Confirm Password</label>
                    <input className="input--form-sign--up" name="Confirm Password" type="password" />

                    <label className="label--form--sign--up">Secret Code</label>
                    <input className="input--form-sign--up" name="Secret Code" type="password" />

                    <input className="submit--form-sign--up" type="submit" value="Register"/>
                </form>

                <hr />
                <small>
                    Already has an account? <span className="login--text--anchor--sign--up">Login here.</span>
                </small>
            </div>

        </section>
    )
}

export default SignUpPage;