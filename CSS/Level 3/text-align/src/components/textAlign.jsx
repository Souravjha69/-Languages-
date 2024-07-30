import classes from "./textAlign.module.css"
function TextAlign () {
    return (
        <div className={classes.main}>
            <div id={classes.box}>
                This is a Box
            </div>
            <a href="#" className={classes.link}>This is a Link.</a>
            <div className={classes.text}>This is my Text</div>
            <div className={classes.paras}>
            <p className={classes.paraOne}>Lorem ipsum dolor sit amet consectetur adipisicing elit. Adipisci cupiditate facilis iure quae ad sit nisi itaque vitae excepturi ipsam?</p>
            <p className={classes.paraTwo}>Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolorum sapiente nobis eligendi eaque, tenetur asperiores fugit repudiandae deleniti iusto voluptatum!</p>
            </div>
        </div>
    );
}
export default TextAlign;