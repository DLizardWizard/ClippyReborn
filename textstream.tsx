import React from "react";

type Props = {};

const a = `Lorem ipsum...`;

const Textstream = (props: Props) => {
  const [state, trigger] = CustomHook(a);

  function handleSubmit(e: any) {
    e.preventDefault();
    trigger();
  }
  return (
    <>
      <div>
        <p style={{ fontSize: "4rem" }}>Text Stream</p>
        <form onSubmit={handleSubmit}>
            <input type="text" style={{ border: '1px solid grey'}}/>
            <input type="submit" name="submit" className="type" />
        </form>
        <p style={{ fontSize: "1rem", fontStyle: "italic" }}>{state}</p>
      </div>
    </>
  );
};

function CustomHook(text: string) {
  const [state, setstate] = useState<any>("");
  const [index, setIndex] = useState(0);
  const [triggerFlag, setTriggerFlag] = useState(false);
  
  useEffect(() => {
    const splittedText = text.split("");
    if (splittedText[index] && triggerFlag)
      setTimeout(() => {
        setstate((prev: any) => {
          return splittedText.slice(0, index).join("");
        });
        setIndex(index + 1);
	}, 100);
  }, [index, state, triggerFlag]);

  function trigger() {
    setTriggerFlag(true);
  }
  
  return [state, trigger];
}

export default Textstream;
