import { useState } from "react";

const ShowTextForm = ({ onAdd,mode }) => {
  const [text, setText] = useState("");

  const onSubmit = (e) => {
    e.preventDefault();

    if (!text) {
      alert("Please add a text");
      return;
    }

    onAdd({ text }, mode);
    setText("");
  };

  return (
    <form className="add-form" onSubmit={onSubmit}>
      <div className="form-control">
        <label>Text</label>
        <input
          type="text"
          placeholder="Adaugati Textul"
          value={text}
          onChange={(e) => setText(e.target.value)}
        />
      </div>

      <input type="submit" value="Verificati" className="btn btn-block" />
    </form>
  );
};

export default ShowTextForm;
