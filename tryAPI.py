import requests  # ייבוא ספריית requests לביצוע בקשות HTTP
import json  # ייבוא ספריית json לטיפול בנתוני JSON
import logging # ייבוא ספריית logging לתיעוד פעולות הקוד

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

def send_request(method, url, payload=None, headers=None, timeout=10):
    """
    שולח בקשת HTTP לכתובת URL שצוינה.

    Args:
        method (str): סוג הבקשה ('GET' או 'POST').
        url (str): כתובת ה-URL לבקשה.
        payload (dict, optional): נתונים לשליחה (לבקשות POST). ברירת מחדל: None.
        headers (dict, optional): כותרות הבקשה. ברירת מחדל: None.
        timeout (int, optional): זמן המתנה בשניות. ברירת מחדל: 10.

    Returns:
        dict or str: תגובת JSON במקרה של הצלחה, או טקסט במקרה של תגובה שאינה JSON.

    Raises:
        ValueError: אם שיטת הבקשה אינה נתמכת.
        Exception: אם הבקשה נכשלה מסיבה כלשהי.
    """
    logger.info(f"שולח בקשת {method} ל-{url}")
    try:
        if method.upper() == "GET":
            response = requests.get(url, timeout=timeout)
        elif method.upper() == "POST":
            response = requests.post(url, json=payload, headers=headers, timeout=timeout)
        else:
            raise ValueError("שיטת בקשה לא נתמכת")

        logger.info(f"סטטוס קוד שהתקבל: {response.status_code}")
        if response.status_code in (200, 201):
            logger.info("בקשה הצליחה!")
            try:
                return response.json()
            except json.JSONDecodeError:
                return response.text
        elif response.status_code == 204:
            logger.info("בקשה הצליחה, אין תוכן בתגובה.")
            return None
        else:
            logger.error(f"שגיאה: סטטוס קוד לא תקין - {response.status_code}")
            logger.error(f"תוכן התגובה: {response.text}")
            raise Exception(f"סטטוס קוד: {response.status_code}")
    except requests.exceptions.RequestException as e:
        logger.error(f"שגיאה בשליחת הבקשה: {e}")
        raise

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/posts"
    payload = {"title": "כותרת לדוגמה", "body": "תוכן לדוגמה", "userId": 1}
    headers = {"Content-Type": "application/json; charset=UTF-8"}

    logger.info("שליחת בקשת GET:")
    get_result = send_request("GET", url)
    if get_result:
        print(json.dumps(get_result, indent=4, ensure_ascii=False))

    logger.info("\nשליחת בקשת POST:")
    post_result = send_request("POST", url, payload, headers)
    if post_result:
        print(json.dumps(post_result, indent=4, ensure_ascii=False))