import React from 'react';
export default class Welcome extends React.Component {
    constructor() {
        super();
        this.state = {
            rows: null,
        };
    }

    async componentDidMount() {
        fetch(`http://localhost:5000/`)
            .then((res) => res.json())
            .then((data) => {
                this.setState({ rows:data.rows });
            });
    }

    render() {
        return <h1 key={'editor'}>{this.state.rows}</h1>;
    }
}