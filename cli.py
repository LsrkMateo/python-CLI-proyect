import  click
import json_manager
@click.group() #Que hace esto??

def cli():
    pass

@cli.command()
def users():
    users = json_manager.read_json()
    for user in users:
        print(f"{user['id']} - {user['name']} - {user['lastname']}")
        

if __name__ == "__main__":
    cli()

