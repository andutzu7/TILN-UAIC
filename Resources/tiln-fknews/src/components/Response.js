
const Response = (response) => {
  return (
    <div>
      <h3>
        {response.response[0].text}
      </h3>
    </div>
  );
};

export default Response;
