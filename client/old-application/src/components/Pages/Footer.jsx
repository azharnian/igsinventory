import React from "react";
import { Link } from "react-router-dom";

export default function Footer(){

    return (
        <footer className="p-3 text-body-secondary text-center text-small bg-dark">
            <p className="mb-1 text-white">&copy; 2023 Ignatius Global School</p>
            <ul className="list-inline">
                <li className="list-inline-item">
                    <Link className="text-decoration-none" to={`/`}>Privacy</Link>
                </li>
                <li className="list-inline-item">
                    <Link className="text-decoration-none" to={`/`}>Terms</Link>
                </li>
                <li className="list-inline-item">
                    <Link className="text-decoration-none" to={`/`}>Support</Link>
                </li>
            </ul>
        </footer>
    )
}