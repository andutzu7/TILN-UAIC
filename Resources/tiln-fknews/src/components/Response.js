import React from "react";
import imgSrc1 from "../images/True.png";
import imgSrc2 from "../images/False.png";

const Response = (response) => {
  return (
    <div>
      {response.response[0].text}
      {response.response[0].text === "true" ? (
        <img className="response" src={imgSrc1} alt={"True Response"} />
      ) : (
        <img className="response" src={imgSrc2} alt={"False Response"} />
      )}
    </div>
  );
};

export default Response;
