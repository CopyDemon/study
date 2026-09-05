import { Mosaic, MosaicWindow } from 'react-mosaic-component';
import 'react-mosaic-component/react-mosaic-component.css';
@import "@blueprintjs/icons/lib/css/blueprint-icons.css";
import '@blueprintjs/core/lib/css/blueprint.css';
import '@blueprintjs/icons/lib/css/blueprint-icons.css';

const TITLE_MAP: Record<ViewId, string> = {
    a: 'Left Window',
    b: 'Top Right Window',
    c: 'Bottom Right Window',
    new: 'New Window',
};

const ELEMENT_MAP: { [viewId: string]: JSX.Element } = {
    a: <div>Flowsheet app</div>,
    b: <div>Top Right Window</div>,
    c: <div>Bottom Right Window</div>,
};

export type ViewId = 'a' | 'b' | 'c' | 'new';
  
const MosaicApp = () => (
    <Mosaic
        renderTile={(id, path) => (
            <MosaicWindow<ViewId> path={path} createNode={() => 'new'} title={TITLE_MAP[id]}>
            </MosaicWindow>
        )}
        initialValue={{
            direction: 'row',
            first: 'a',
            second: {
                direction: 'column',
                first: 'b',
                second: 'c',
            },
            splitPercentage: 40,
        }}
    />
  );


export default MosaicApp