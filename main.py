import pixela
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("TOKEN")
NAME = os.getenv("NAME")
GRAPH_ID = os.getenv("GRAPH_ID")

pixela = pixela.Pixela()
# pixela.update_pixela_pixel(NAME, GRAPH_ID, TOKEN, "20220724", "100")
# pixela.delete_pixela_pixel(username=NAME, graph_id=GRAPH_ID, date="20220724", token=TOKEN)
pixela.create_pixela_pixel(username=NAME, graph_id=GRAPH_ID, token=TOKEN, qty="500")