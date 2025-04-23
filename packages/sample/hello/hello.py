def main(args):
      name = args.get("name", "stranger")
      greeting = "Hello " + name + "! welcome to DO"
      print(greeting)
      return {"body": greeting}
  
