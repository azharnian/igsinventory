import { Link } from "react-router-dom";

import 'bootstrap/dist/css/bootstrap.css';


export default function Header(){
    return (
    <header className="navbar sticky-top bg-dark flex-md-nowrap p-0 shadow" data-bs-theme="dark">
        <Link className="navbar-brand col-md-3 col-lg-2 me-0 px-3 fs-6 text-white" to={`/dashboard`}>
            Inventory System
        </Link>

    </header>
    )
}