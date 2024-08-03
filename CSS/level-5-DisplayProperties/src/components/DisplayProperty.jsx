import classes from "./DisplayProperty.module.css";

function DisplayProperty() {
    return (
        <div className={classes.mainone}>
            <h3>Learning Dipslay Inline or Block Property</h3>
        <div className={classes.boxes}>
            <div id={classes.box1} className={classes.box}>Box 1</div>
            <div id={classes.box2} className={classes.box}>Box 2</div>
        </div>
        </div>
    );
}
export default DisplayProperty;