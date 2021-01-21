import React, { Component } from "react";

const list = [
  {
    "id": 1,
    "title": "Investigate 500 error for site",
    "body": "Getting a 500 error when navigating to 'About Us' section."
  },
  {
    "id": 2,
    "title": "Add contact form to 'Contact Us' section",
    "body": "Add a contact form to the contact section. Make sure to add correct model as well."
  },
  {
    "id": 3,
    "title": "Clean up search feature", "body": "Limit output of available search queries for search feature."
  }
];

class App extends Component {
  constructor(props) {
    super(props);
    this.state = { list }
  }

  render() {
    return (
      <div>
        {this.state.list.map(item => (
          <div key={item.id}>
            <h1>{item.title}</h1>
            <p>{item.body}</p>
          </div>
        ))}
      </div>
    )
  }
}

export default App;