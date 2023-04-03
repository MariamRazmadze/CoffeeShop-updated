import classes from './CoffeeSummary.module.css';

const CoffeeSummary = () =>{
    return(
    <section className={classes.summary}>
    <h2>Espresso Bar</h2>
    <p>All drinks can be Hot or Iced, and specialty drinks can be blended.  Add an extra shot or almond/oat/soy milk or syrup for $0.75</p>
    <p>We only use Fresh Organic Espresso Beans! </p>
    </section>
    );
};

export default CoffeeSummary;