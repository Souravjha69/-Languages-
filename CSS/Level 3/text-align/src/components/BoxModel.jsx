import classes from "./BoxModel.module.css";

function Boxmodel () {
    return (
        <div className={classes.main}>
            <h2>Padding Property</h2>
            <div id={classes.first}className={classes.pad}>Padding Checker</div>
            <div id={classes.second} className={classes.pad}>Padding Checker</div>
        </div>
    );
}

export default Boxmodel;