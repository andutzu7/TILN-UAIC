import React from "react";

const Response = (response) => {
  return (
    <div>
      {response.response[0].text}
      {response.response[0].text == "true" ? (
        <imd src={require("../images/True.png")} alt="True Response" />
      ) : (
        <imd src={require("../images/False.png")} alt="False Response" />
      )}
    </div>
  );
};

export default Response;
