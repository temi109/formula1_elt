create_circuits_table = """
    CREATE OR REPLACE TRANSIENT TABLE {{ params.table_name }}
        (
            circuitId VARCHAR,
            circuitRef VARCHAR,
            name VARCHAR,
            location VARCHAR,
            country VARCHAR,
            lat int,
            lng int,
            alt int,
            url VARCHAR
        );
"""

create_races_table = """
    CREATE OR REPLACE TRANSIENT TABLE {{ params.table_name }}
        (
            raceId VARCHAR ,
            year int,
            round int,
            circuitId int,
            name VARCHAR,
            date date,
            time VARCHAR,
            url VARCHAR

            );
"""

create_constructors_table = """
    CREATE OR REPLACE TRANSIENT TABLE {{ params.table_name }}
    (
    constructorId VARCHAR ,
    constructorRef VARCHAR,
    name VARCHAR,
    nationality VARCHAR,
    url VARCHAR
    );

"""


create_results_table = """
    CREATE OR REPLACE TRANSIENT TABLE {{ params.table_name }}
    (
        resultId VARCHAR,
        raceId VARCHAR,
        driverId VARCHAR,
        constructorId VARCHAR,
        number int,
        grid int,
        position int,
        positionText int,
        positionOrder int,
        points int,
        laps int,
        time VARCHAR,
        milliseconds int,
        rank int
    );
"""



start_warehouse = """
    CREATE OR REPLACE WAREHOUSE my_wh WAREHOUSE_SIZE=XSMALL INITIALLY_SUSPENDED=FALSE
    AUTO_SUSPEND = 300;
"""

drop_warehouse = """
    DROP WAREHOUSE my_wh;
"""
