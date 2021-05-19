import React from "react";

const Response = (response) => {
  return (
    <div className="response">
      {response.response[0].text}
      {response.response[0].text == "true" ? (
        <img src={require("../images/True.png")} alt="True Response" />
      ) : (
        <img src={require("../images/False.png")} alt="False Response" />
      )}
    </div>
  );
};

export default Response;
