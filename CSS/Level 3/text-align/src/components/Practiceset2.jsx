import classes from "./BoxModel.module.css";
function Practiceset () {
    return (
        <div className={classes.maintwo}>
            <div className={classes.pra}>
                Sourav
            </div>
            <button className={classes.button}>Click</button>
            <div className={classes.boxOne}><h3>Box1</h3></div>
            <div className={classes.boxTwo}>Box 2</div>
        </div>
    );
}

export default Practiceset;