import React from 'react';

import './Header.css';
import InformationHeader from './SubHeader/InformationHeader/InformationHeader';
import MainHeader from './SubHeader/MainHeader/MainHeader';


class Header extends React.Component {
    render = () => {
        return (
            <header>
                <InformationHeader />
                <MainHeader />
            </header>
        )
    }
}

export default Header;