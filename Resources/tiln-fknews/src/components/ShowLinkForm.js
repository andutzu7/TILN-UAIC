import { useState } from "react";

const ShowLinkForm = ({ onAdd }) => {
  const [text, setText] = useState("");

  const onSubmit = (e) => {
    e.preventDefault();

    if (!text) {
      alert("Please add a link");
      return;
    }

    onAdd({ text });
    setText("");
  };

  return (
    <form className="add-form" onSubmit={onSubmit}>
      <div className="form-control">
        <label>Link</label>
        <input
          type="text"
          placeholder="Adaugati Link"
          value={text}
          onChange={(e) => setText(e.target.value)}
        />
      </div>

      <input type="submit" value="Verificati" className="btn btn-block" />
    </form>
  );
};

export default ShowLinkForm;
