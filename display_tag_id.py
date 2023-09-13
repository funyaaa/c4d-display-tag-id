def main():
    obj = doc.GetActiveObject()
    if not obj:
        print("Please select an object.")
        return
    
    tag = obj.GetFirstTag()
    while tag:
        print(f"Tag Name: {tag.GetName()}, Tag ID: {tag.GetType()}")
        tag = tag.GetNext()

if __name__=='__main__':
    main()