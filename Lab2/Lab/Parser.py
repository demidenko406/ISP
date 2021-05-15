from Lab.Sereializer import Serializer # pragma: no cover
import argparse # pragma: no cover

def main():# pragma: no cover
    parser = argparse.ArgumentParser(description="ArgParser")# pragma: no cover
    parser.add_argument('src', type=str, help='Source file')# pragma: no cover
    parser.add_argument('dest', type=str, help='Destination file')# pragma: no cover
    parser.add_argument('ext', type=str, help='New file extension')# pragma: no cover

    argv = parser.parse_args()# pragma: no cover

    src_ext = argv.src.split('.')[-1]# pragma: no cover

    if src_ext == argv.ext.lower():# pragma: no cover
        pass# pragma: no cover
    else:# pragma: no cover
        load_serializer = Serializer(src_ext)# pragma: no cover
        dump_serializer = Serializer(argv.ext)# pragma: no cover
        obj = load_serializer.load(argv.src)# pragma: no cover
        dump_serializer.dump(obj,argv.dest)# pragma: no cover

if __name__ == "__main__":# pragma: no cover
    main()# pragma: no cover
