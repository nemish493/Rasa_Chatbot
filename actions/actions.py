# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionOverview(Action):

    def name(self) -> Text:
        return "action_overview"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        message = "We offer a variety of language and elective courses, including specialized programs."
        dispatcher.utter_message(text=message)

        return []

class ActionOverviewAwp(Action):

    def name(self) -> Text:
        return "action_overview_awp"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        message = ("To get more info on AWP subject and compulsory language courses:"
                   "(https://www.th-deg.de/Studierende/AWP-Sprachkurse/Uebersicht_AWP-_und_Sprachenwahl_DEG.pdf)")
        dispatcher.utter_message(text=message)

        return []

class ActionElectiveOverview(Action):

    def name(self) -> Text:
        return "action_elective_overview"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        message = ("An elective (AWP) is a compulsory elective subject of a general academic nature prescribed by the study and examination regulations, which must be successfully completed.")
        dispatcher.utter_message(text=message)

        return []

class ActionCompulsoryOverview(Action):

    def name(self) -> Text:
        return "action_compulsory_overview"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        message = ("a compulsory language course is prescribed in the study and examination regulations for the respective course of study and must be successfully completed by the end of the studies.")
        dispatcher.utter_message(text=message)

        return []

class ActionLectureSchedule(Action):

    def name(self) -> Text:
        return "action_lecture_schedule"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        message = "The lecture schedules are updated every semester and can be found on our website."
        dispatcher.utter_message(text=message)

        return []


class ActionLectureExamInfo(Action):

    def name(self) -> Text:
        return "action_lecture_exam_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        message = ("Dates for examination registration are announced on the DIT website. As with other examinations, "
                   "registration takes place via the Primuss portal.(https://www.primuss.de/portal-thd)")
        dispatcher.utter_message(text=message)

        return []


class ActionLanguageOffer(Action):

    def name(self) -> Text:
        return "action_language_offer"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        message = "We offer German, English, French, and Spanish courses."
        dispatcher.utter_message(text=message)

        return []


class ActionIntensiveLanguageCourse(Action):

    def name(self) -> Text:
        return "action_intensive_language_course"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        message = ("Our intensive language courses are designed for rapid language acquisition."
                   "Dates for examination registration are announced on the DIT website. As with other examinations, "
                   "registration takes place via the Primuss portal.[here](https://www.primuss.de/portal-thd)")
        dispatcher.utter_message(text=message)

        return []

class ActionCourseSelection(Action):

    def name(self) -> Text:
        return "action_course_selection"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        message = "Before the semester begins, you can register for compulsory language courses, AWP (elective courses), as well as voluntary subsidiary subjects."
        dispatcher.utter_message(text=message)

        return []

class ActionContact(Action):

    def name(self) -> Text:
        return "action_contact"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        message = "For more question you can contact AWP CENTRE [here](sprachenzentrum@th-deg.de)"
        dispatcher.utter_message(text=message)

        return []
