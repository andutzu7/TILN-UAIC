import { FaTimes } from "react-icons/fa";

const Response = (response) => {
  return (
    <div>
      <h3>
        {response.text} <FaTimes style={{ color: "red", cursor: "pointer" }} />
      </h3>
    </div>
  );
};

export default Response;
