import chromadb
chroma_client = chromadb.Client()

collection = chroma_client.create_collection(name="wood_collection")

wood_summaries = [
    {
        "Title": "Oak",
        "Description": "Oak is a strong, durable hardwood with a prominent grain pattern.",
        "Uses in Builds": "Flooring, cabinetry, and structural beams.",
        "Uses in Furniture": "Tables, chairs, and cabinets.",
        "Uses in General Goods": "Barrels, veneers, and tool handles."
    },
    {
        "Title": "Maple",
        "Description": "Maple is a dense, durable wood with a fine, even texture.",
        "Uses in Builds": "Flooring, cabinets, and butcher blocks.",
        "Uses in Furniture": "Dressers, tables, and musical instruments.",
        "Uses in General Goods": "Cutting boards, bowling pins, and skateboards."
    },
    {
        "Title": "Cherry",
        "Description": "Cherry wood has a rich, reddish-brown color that darkens with age.",
        "Uses in Builds": "Paneling and trim.",
        "Uses in Furniture": "Fine furniture, cabinets, and musical instruments.",
        "Uses in General Goods": "Carvings, veneers, and small specialty items."
    },
    {
        "Title": "Pine",
        "Description": "Pine is a softwood known for its light color and straight grain.",
        "Uses in Builds": "Construction lumber, paneling, and roofing.",
        "Uses in Furniture": "Rustic furniture, shelving, and cabinets.",
        "Uses in General Goods": "Crates, boxes, and toys."
    },
    {
        "Title": "Walnut",
        "Description": "Walnut is a strong, dark wood with a fine, straight grain.",
        "Uses in Builds": "High-end cabinetry and flooring.",
        "Uses in Furniture": "Fine furniture, desks, and tables.",
        "Uses in General Goods": "Gun stocks, musical instruments, and veneers."
    },
    {
        "Title": "Mahogany",
        "Description": "Mahogany is a reddish-brown hardwood known for its beauty and durability.",
        "Uses in Builds": "Boat building and high-end millwork.",
        "Uses in Furniture": "High-end furniture, cabinets, and musical instruments.",
        "Uses in General Goods": "Carvings, veneers, and specialty items."
    },
    {
        "Title": "Birch",
        "Description": "Birch is a strong hardwood with a smooth, fine grain.",
        "Uses in Builds": "Plywood and interior finishes.",
        "Uses in Furniture": "Cabinets, tables, and chairs.",
        "Uses in General Goods": "Toys, model airplanes, and drum shells."
    },
    {
        "Title": "Teak",
        "Description": "Teak is a durable hardwood with natural oils that make it resistant to water and pests.",
        "Uses in Builds": "Boat building and outdoor structures.",
        "Uses in Furniture": "Outdoor furniture, flooring, and countertops.",
        "Uses in General Goods": "Cutting boards, countertops, and carvings."
    },
    {
        "Title": "Cedar",
        "Description": "Cedar is a softwood known for its aromatic scent and resistance to decay.",
        "Uses in Builds": "Siding, shingles, and outdoor structures.",
        "Uses in Furniture": "Closets, chests, and outdoor furniture.",
        "Uses in General Goods": "Aromatic boxes, pet bedding, and garden items."
    },
    {
        "Title": "Ash",
        "Description": "Ash is a tough, elastic hardwood with a straight grain.",
        "Uses in Builds": "Tool handles and sports equipment.",
        "Uses in Furniture": "Cabinets, chairs, and tables.",
        "Uses in General Goods": "Baseball bats, oars, and flooring."
    }
]

# Create document strings and IDs
documents = []
ids = []

for i, wood in enumerate(wood_summaries):
    doc = f"""
    Title: {wood['Title']}
    Description: {wood['Description']}
    Uses in Builds: {wood['Uses in Builds']}
    Uses in Furniture: {wood['Uses in Furniture']}
    Uses in General Goods: {wood['Uses in General Goods']}
    """
    documents.append(doc.strip())
    ids.append(f"id{i+1}")

# Format the output for collection.add
output = f"""collection.add(
    documents={documents},
    ids={ids},
)"""

# Print the output
print(output)

collection.add(
    documents=documents,
    ids=ids,
)

results = collection.query(
    query_texts=["This is a query document about hardwood for flooring"],  # Chroma will embed this for you
    n_results=2  # how many results to return
)

print(results)