def save_to_file(file_name, jobs):
    file = open(f"{file_name}.csv", mode="w")
    file.write("title,company,region,position")

    for job in jobs:
        file.write(
            f"{job['title']},{job['company']},{job['region']},{job['position']}\n"
        )

    file.close()
