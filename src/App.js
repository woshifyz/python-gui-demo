import logo from './logo.svg';
import './App.css';

function App() {
   const cli = async () => {
       let resp = await window.pywebview.api.open_file_dialog();
       console.log(resp);
   }
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p className="text-3xl font-bold underline">
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
        <button onClick={() => {cli()}}>xxxx</button>
      </header>
    </div>
  );
}

export default App;
