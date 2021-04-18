import { useState, useEffect } from "react";
import { BrowserRouter as Router, Route } from "react-router-dom";
import Header from "./components/Header";
import ShowTextForm from "./components/ShowTextForm";
import ShowLinkForm from "./components/ShowLinkForm";
import Response from "./components/Response";
import Footer from "./components/Footer";
import About from "./components/About";

const App = () => {
  const [showTextForm, setShowTextForm] = useState(false);
  const [showLinkForm, setShowLinkForm] = useState(false);
  const [response, setResponse] = useState([]);

  // Verify Text
  const verifyText = async (text) => {
    const res = await fetch("http://localhost:5000/tasks", {
      method: "POST",
      headers: {
        "Content-type": "application/json",
      },
      body: JSON.stringify(text),
    });

    const data = await res.json();

    setResponse([...response, data]);
  };

  // Verify Link
  const verifyLink = async (text) => {
    const res = await fetch("http://localhost:5000/tasks", {
      method: "POST",
      headers: {
        "Content-type": "application/json",
      },
      body: JSON.stringify(text),
    });

    const data = await res.json();

    setResponse([...response, data]);
  };

  return (
    <Router>
      <div className="container">
        <Header
          onText={() => setShowTextForm(!showTextForm)}
          showText={showTextForm}
          onLink={() => setShowLinkForm(!showLinkForm)}
          showLink={showLinkForm}
        />
        <Route
          path="/"
          exact
          render={(props) => (
            <>
              {showTextForm && <ShowTextForm onAdd={verifyText} />}
              {showLinkForm && <ShowLinkForm onAdd={verifyLink} />}
              {response.length > 0 ? (
                <Response response={response} />
              ) : (
                "Verificati un articol"
              )}
            </>
          )}
        />
        <Route path="/about" component={About} />
        <Footer />
      </div>
    </Router>
  );
};

export default App;
