import PropTypes from "prop-types";
import { useLocation } from "react-router-dom";
import Button from "./Button";

const Header = ({ title, onText, showText, onLink, showLink }) => {
  const location = useLocation();

  return (
    <header className="header">
      <h1>{title}</h1>
      {location.pathname === "/" && (
        <Button
          color={showText ? "red" : "green"}
          text={showText ? "Close" : "Text"}
          onClick={onText}
        />
      )}
      {location.pathname === "/" && (
        <Button
          color={showLink ? "red" : "green"}
          text={showLink ? "Close" : "Link"}
          onClick={onLink}
        />
      )}
    </header>
  );
};

Header.defaultProps = {
  title: "Detectarea Articolelor False",
};

Header.propTypes = {
  title: PropTypes.string.isRequired,
};

export default Header;
