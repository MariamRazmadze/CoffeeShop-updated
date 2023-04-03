import CoffeeSummary from "./CoffeeSummary";
import AvailableCoffee from "./AvailableCoffee";
import { Fragment } from "react";

const Coffee = () =>{
    return <Fragment>
        <CoffeeSummary/>
        <AvailableCoffee />
    </Fragment>
}

export default Coffee;