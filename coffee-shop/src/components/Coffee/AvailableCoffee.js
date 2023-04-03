import classes from "./AvailableCoffee.module.css";
import Card from "../UI/Card";
import CoffeeItem from "./CoffeeItem/CoffeeItem";
import { useEffect, useState } from "react";

const AvailableCoffee = () => {
  const [coffeeItems, setCoffeeItems] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [httpError, setHttpError] = useState();
  useEffect(() => {
    const fetchCoffee = async () => {
      const response = await fetch("http://localhost:5000/product");

      if (!response.ok) {
        throw new Error("Something went wrong!");
      }
      const responseData = await response.json();

      const loadedCoffee = [];

      for (const key in responseData) {
        loadedCoffee.push({
          id: key,
          name: responseData[key].name,
          description: responseData[key].description,
          price: responseData[key].price,
        });
      }
      setCoffeeItems(loadedCoffee);
      setIsLoading(false);
    };

    fetchCoffee().catch((error) => {
      setIsLoading(false);
      setHttpError(error.message);
    });
  }, []);

  if (isLoading) {
    return (
      <section className={classes.coffeeLoading}>
        <p>Loading...</p>
      </section>
    );
  }

  if (httpError) {
    return (
      <section className={classes.coffeeError}>
        <p>{httpError}</p>
      </section>
    );
  }
  const coffeeList = coffeeItems.map((coffee) => (
    <CoffeeItem
      key={coffee.id}
      id={coffee.id}
      name={coffee.name}
      description={coffee.description}
      price={coffee.price}
    />
  ));
  return (
    <section className={classes.coffee}>
      <Card>
        <ul>{coffeeList}</ul>
      </Card>
    </section>
  );
};

export default AvailableCoffee;
