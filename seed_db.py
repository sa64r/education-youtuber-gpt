from utils import clear_db, get_or_create_collection, load_chroma_client

client = load_chroma_client()

clear_db(client)

test_collection = get_or_create_collection("test", client)


test_collection.add(
    documents=[
        "To make a sandwich you need to put bread together",
        "Building a plane is very hard",
        "The tallest building in the world is the Burj Khalifa",
        "Keval was born in london",
        "Keval's favourite food is pizza",
        "Keval's favourite colour is blue",
        "Keval's favourite animal is a dog",
        "Keval's favourite sport is football",
        "Keval's favourite subject is maths",
        "Keval's favourite game is minecraft",
        "Keval's favourite movie is the matrix",
        "Keval lives with a flatmate called Suraj",
    ],
    ids=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"],
)

ali_collection = get_or_create_collection("ali-abdaal", client)

ali_collection.add(
    documents=[
        "Ali Abdaal is a doctor",
        "Ali Abdaal is a YouTuber",
        "Ali Abdaal went to Cambridge",
        "Ali Abdaal is from Cambridge",
        "Ali Abdaal is a medical doctor",
        "Ali Abdaal has a brother called Taimur",
        "If you want to be a doctor you need to study medicine",
        "To be a good doctor you need to be good at science",
        "To be a good doctor you need to be good at maths",
        "To be a good doctor you need to be good at biology",
        "To be a good doctor you need to be good at chemistry",
    ],
    ids=[
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "11",
    ],
)
