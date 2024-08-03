import classes from "./Responsive.module.css";

function Responsive () {
    return (
        <div className={classes.main}>
            <h3>Relative Unit : Responsiveness</h3>
            <div className={classes.first}>
                First Div
                <div className={classes.second}>
                    Second Div
                </div>
            </div>
        </div>
    );
}
export default Responsive;