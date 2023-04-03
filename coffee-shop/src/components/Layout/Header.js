import { Fragment } from "react";
import coffeeImage from '../../assets/header.jpg';
import classes from './Header.module.css';
import HeaderCartButton from "./HeaderCartButton";



const Header = props =>{
    return <Fragment>
        <header className={classes.header}>
            <h1>Java Joe's</h1>
            <HeaderCartButton onClick={props.onShowCart} />
        </header>
        <div className={classes['main-image']}>
            <img src={coffeeImage} alt='2 coffees. actually  hot chocolates'/>

        </div>
    </Fragment>
};

export default Header;