import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faLinkedin, faGithub } from "@fortawesome/free-brands-svg-icons";
import classes from "./PracticeSet.module.css";
import { faCode } from "@fortawesome/free-solid-svg-icons";

function PracticeSet() {
    return (
        <div className={classes.heading}>
            <h2>Practice Set Text Properties</h2>
            <div className={classes.outer}> This is Outer Div here
                <div className={classes.inner}> This is Inner div here.</div>
            </div>
            <h4>Setting the Icons:- LinkedIn <FontAwesomeIcon icon={faLinkedin} /></h4>
            <h4>Github Icon : - <FontAwesomeIcon icon={faGithub} /></h4>
            <h4>This is Code icon here: - <FontAwesomeIcon icon={faCode} /></h4>
        </div>
    );
}

export default PracticeSet;
