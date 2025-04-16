def new_resizer(max_width, max_height):
    
    def mins(min_width = 0, min_height = 0):
        if min_width > max_width or min_height > max_height:
            raise Exception("minimum size cannot exceed maximum size")
        def size(width, height):

            return width, height
            
        return size
        
    return mins
