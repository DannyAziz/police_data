import csv, glob, time

from .models import StopAndSearch


def csv_row_to_stop_and_search(row, force):
    StopAndSearch.objects.create(
        force=force,
        type=row[0],
        datetime=row[1],
        operation=row[2] if (row[2] != '') else False,
        operation_name=row[3],
        latitude=row[4],
        longitude=row[5],
        gender=row[6],
        age_range=row[7],
        self_defined_ethnicity=row[8],
        officer_defined_ethnicity=row[9],
        legislation=row[10],
        object_of_search=row[11],
        outcome=row[12],
        outcome_linked_to_object_of_search=row[13],
        removal_of_more_than_outer_clothing=row[14],
    )


def populate_metropolitan_stop_searches():
    function_start = time.time()
    files = glob.glob("police_datasets/**/*stop-and-search.csv", recursive=True)

    num_of_files = len(files)
    file_iteration_count = 0

    for file in files:
        loop_start = time.time()
        file_iteration_count += 1
        print("Number of Files: {count}".format(count=num_of_files))
        print("Current Iteration: {count}".format(count=file_iteration_count))

        with open(file, newline='') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',')
            for idx, row in enumerate(csv_reader):
                if idx == 0:
                    continue
                csv_row_to_stop_and_search(row, "metropolitan")

        loop_end = time.time()
        print("Loop Took: {time_taken} Seconds".format(time_taken=loop_end-loop_start))

    function_end = time.time()

    print("Function Took: {time_taken} Seconds".format(time_taken=function_end-function_start))
    return True
