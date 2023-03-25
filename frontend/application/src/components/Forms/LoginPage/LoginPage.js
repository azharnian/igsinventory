import "./LoginPage.css"

function LoginPage(){

    return (
        <section className="page--login">

            <div className="main--box--login">

                <h1>
                    Login Into Your Account
                </h1>

                <form className="form--login">

                    <label className="label--form--login">Username</label>
                    <input className="input--form-login" name="Username" type="text" autoFocus />

                    <label className="label--form--login">Password</label>
                    <input className="input--form-login" name="Password" type="password" />

                    <input className="submit--form-login" type="submit" value="Log In"/>
                </form>

                <hr />
                <small>
                    Don't have an account? <span className="signup--text--anchor--login">Register here.</span>
                </small>
            </div>

        </section>
    )
}

export default LoginPage;