import { useState, useEffect } from "react";

export default function App() {
  const [data, setData] = useState([{}]);

  useEffect(() => {
    fetch(`${import.meta.env.VITE_BACKEND_URL || ""}/api/user`)
      .then((res) => res.json())
      .then((data) => {
        setData(data);
        console.log(data);
      });
  }, []);

  return (
    <div>
      <h1>Hello {data.name}</h1>
    </div>
  );
}
